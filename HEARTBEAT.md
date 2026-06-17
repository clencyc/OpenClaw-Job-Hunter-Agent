# Hourly Routine
1. Execute the `search_and_apply_jobs` tool to find new listings matching the JD.
2. For any successful submission, use the `append_to_google_sheet` tool.
3. Message the user on WhatsApp with a summary of actions taken. If no applications were processed, respond with `HEARTBEAT_OK` to keep the chat quiet.