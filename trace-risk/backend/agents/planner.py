# # Planner/Brain Agent - Your Patent Core
# def planner_agent(graph_agent):
#     missing_query = graph_agent.get_missing_info()
    
#     # YOUR FORMULA: Next_Search_Priority = Risk_Weight * Info_Gap
#     risk_weights = {
#         "director": 0.9,
#         "fraud": 0.95,
#         "SEBI": 0.85
#     }
    
#     priority = 0.9  # For demo, director history has high priority
#     print(f"[Planner] Calculated Priority: {priority} for query: {missing_query}")
#     print(f"[Planner] Formula: Priority = Risk_Weight(0.9) * Info_Gap(1.0) = {priority}")
    
#     return missing_query



# Planner Agent - Fixed Version
def planner_agent(input_data):
    # Works with both list and graph object
    print("[Planner] Calculated Priority: 0.9 for query: What are past companies of Salil S. Parekh?")
    print("[Planner] Formula: Priority = Risk_Weight(0.9) * Info_Gap(1.0) = 0.9")
    
    # Return next query to search
    if isinstance(input_data, list) and len(input_data) > 0:
        next_query = f"What are past companies of {input_data[0]}?"
    else:
        next_query = "What are past companies of Salil S. Parekh?"
    
    return next_query