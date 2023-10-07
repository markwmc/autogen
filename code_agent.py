from autogen import config_list_from_json
import autogen
import tkinter as tk

# Get api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
llm_config = {"config_list": config_list, "seed":42, "request_timeout": 120}

# Create user proxy agent, coder, product manager
user_proxy = autogen.UserProxyAgent (
    name="User_Proxy",
    system_message="A human admin who will give the idea and run the code provided by Coder.",
    code_execution_config={"last_n_messages": 20, "work_dir": "groupchat", "use_docker": False},
    human_input_mode="NEVER",  
)

coder = autogen.AssistantAgent(
    name="Coder",
    system_message="You will build the code",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="product_manager",
    system_message="You will help break down the initial idea into a well scoped requirement for the coder; Do not involve in future converstaions or error fixing.",
    llm_config=llm_config,
) 

# Create groupchat
groupchat = autogen.GroupChat(
    agents=[user_proxy, coder, pm], messages=[]
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Start the conversation
user_proxy.initiate_chat(
    manager, message="Build a classic & basic pong game with 2 players in python"
)