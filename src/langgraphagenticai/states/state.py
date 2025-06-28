from pydantic import BaseModel, Field
from typing_extensions import TypedDict, List
from langgraph.


class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    message: Annotated[List, add_messages]