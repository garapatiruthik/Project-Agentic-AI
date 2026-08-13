========================================================================================================================
                                     SYSTEM ARCHITECTURE & WORKFLOW VISUALIZATION
========================================================================================================================

 ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
 │  LAYER 1: INTERFACE & PRESENTATION LAYER                                                                           │
 │  (Streamlit / Next.js + FastAPI) [cite: 28, 89]                                                                    │
 └─────────────────────────────────────────┬──────────────────────────────────────────────────────────────────────────┘
                                           │ User Input (Prompt, Budget, Dates, Preferences) [cite: 1, 4]
                                           ▼
 ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
 │  LAYER 2: STATE & ORCHESTRATION LAYER (LangGraph StateGraph) [cite: 2, 66, 94]                                     │
 │  Shared State: { preferences, transport_options, hotel_options, itinerary, total_cost, budget_approved } [cite: 59, 67, 95]│
 └──────┬─────────────────────────────────────────────────────────────────────────────────────────▲───────────────────┘
        │                                                                                         │
        │ [STEP 1] Raw Input                                                                      │ [RE-ENTRY / LOOP]
        ▼                                                                                         │ Downgrade Prompt
 ┌─────────────────────────────────────────────────────────────────────────────────────────────┐  │ (e.g., "Find stays
 │  LAYER 3: AGENT WORKER LAYER [cite: 71, 96]                                                 │  │  under $60/night")
 │                                                                                             │  │  [cite: 16, 115]
 │  ┌───────────────────────────────────────────────────────────────────────────────────────┐  │  │
 │  │ STEP 1: INTAKE & PARSER NODE [cite: 71, 100]                                          │  │  │
 │  │ • Parses: Origin, Destination, Dates, Max Budget, Interests, Tier [cite: 4, 72, 102]  │  │  │
 │  └─────────────────────────────────────────┬─────────────────────────────────────────────┘  │  │
 │                                            │ Structured Preferences [cite: 4, 72]          │  │
 │                                            ▼                                                │  │
 │  ┌───────────────────────────────────────────────────────────────────────────────────────┐  │  │
 │  │ STEP 2: TRANSPORT AGENT [cite: 5, 73, 103]                                            │  │  │
 │  │ • Searches: Flights, trains, and buses (cheapest to mid-range) [cite: 5, 73, 105]     │  │  │
 │  │ • Output: Top 3 travel options with exact prices [cite: 7, 74, 105]                    │  │  │
 │  └─────────────────────────────────────────┬─────────────────────────────────────────────┘  │  │
 │                                            │ Selected Transport Data [cite: 7, 74]          │  │
 │                                            ▼                                                │  │
 │  ┌───────────────────────────────────────────────────────────────────────────────────────┐  │  │
 │  │ STEP 3: ACCOMMODATION & REVIEW AGENT [cite: 8, 75, 106]                               │──┼──┘
 │  │ • Searches: Hotels & stays matching tier constraints [cite: 8, 76, 108]               │  │
 │  │ • Output: Top 3 hotel options + sentiment/review summaries [cite: 10, 75, 76, 108]    │  │
 │  └─────────────────────────────────────────┬─────────────────────────────────────────────┘  │
 │                                            │ Selected Hotel Data [cite: 10, 76]             │
 │                                            ▼                                                │
 │  ┌───────────────────────────────────────────────────────────────────────────────────────┐  │
 │  │ STEP 4: EXPERIENCE & VIBE CURATOR [cite: 11, 77, 109]                                 │  │
 │  │ • Curates: Daily activities tailored to tags (Pubs, History, Foodie) [cite: 12, 13, 77, 78, 111]│
 │  │ • Output: Detailed daily route & scheduled itinerary [cite: 111]                      │  │
 │  └─────────────────────────────────────────┬─────────────────────────────────────────────┘  │
 │                                            │ Complete Draft Itinerary & Costs [cite: 80, 113]│
 │                                            ▼                                                │
 │  ┌───────────────────────────────────────────────────────────────────────────────────────┐  │
 │  │ STEP 5: BUDGET & CONSTRAINT AUDITOR (VALIDATION GUARDRAIL) [cite: 15, 80, 112, 113]  │  │
 │  │ • Computes: Total = Transport Cost + Hotel Cost + Daily Allowance  │  │
 │  └─────────────────────────────────────────┬─────────────────────────────────────────────┘  │
 └────────────────────────────────────────────┼────────────────────────────────────────────────┘
                                              │
                         ┌────────────────────┴────────────────────┐
                         │ CONDITIONAL ROUTING EVALUATION [cite: 81, 88, 114] │
                         └────────────────────┬────────────────────┘
                                              │
                   ┌──────────────────────────┴──────────────────────────┐
                   │                                                     │
      [IF TOTAL > MAX BUDGET]                               [IF TOTAL <= MAX BUDGET]
    (Budget Exceeded) [cite: 16, 81, 114]                 (Budget Approved) [cite: 59, 67, 95]
                   │                                                     │
                   ▼                                                     ▼
┌──────────────────────────────────────┐              ┌──────────────────────────────────────┐
│  RE-TRIGGER FEEDBACK LOOP [cite: 3, 81, 114]│       │  SYNTHESIZE FINAL ITINERARY          │
│  Sends downgrade feedback back to    │              │  Outputs final markdown plan, map    │
│  Accommodation/Transport Agents      │              │  routes, and expense breakdowns      │
│  [cite: 16, 81, 114, 115]            │              │  [cite: 27, 90]                      │
└──────────────────────────────────────┘              └──────────────────┬───────────────────┘
                                                                         │
                                                                         ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  LAYER 4: INTEGRATION LAYER (MODEL CONTEXT PROTOCOL / MCP TOOLS)                                                   │                
│                                                                                                                    │
│  ┌─────────────────────────┐     ┌─────────────────────────────┐     ┌──────────────────────────────────────────┐  │
│  │ Travel/Skyscanner MCP   │     │ Google Maps MCP             │     │ Brave / Tavily / DuckDuckGo Search MCP   │  │
│  │ Server                  │     │ Server                      │     │ Server                                   │  │
│  │ (Flight/Hotel Prices)   │     │ (Distances, Route Maps,     │     │ (Real-time Reviews, Pub/Food Blogs)      │  │
│  │ [cite: 6, 9, 20, 84]    │     │ Spatial Logistics)          │     |                                          │  │
│  └─────────────────────────┘     └─────────────────────────────┘     └──────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
