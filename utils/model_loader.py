# from config_loader import 
import os 
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, Optional,Any
from utils.config_loader import load_config
from langchain_groq import ChatGroq 
 
class ConfigLoader:
    def __init__(self):
        print(f"Loading config....")
        self.config = load_config()

    def __getitem__(self,key):## This method allows you to access config values using dictionary-like syntax
        return self.config[key]
    

class ModelLoader(BaseModel):
    model_provider: Literal["groq"] = "groq" 
    config: Optional[ConfigLoader] = Field(default = None, exclude = True) # either the config is ConfigLoader object or None

    def model_post_init(self, __context: Any)->None:
        self.config = ConfigLoader()   # model_post_init is a Pydantic V2 hook, which runs after model creation.It assigns a ConfigLoader() instance to self.config.This ensures the configuration is loaded whenever you create a ModelLoader.

    class Config:
        arbitrary_types_allowed = True  # Allows ConfigLoader (a non-Pydantic class) to be used as a field in the model.

    def load_llm(self):
        """
        Load and return the LLM model
        """
        print("LLM loading...")
        print("Loading model from provider: ")
        if self.model_provider == "groq":
            print("Loading model from GROQ:")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model = model_name, api_key = groq_api_key)
        return llm

    
         
