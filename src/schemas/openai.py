from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Union, Dict, Any, Literal


class ChatMessage(BaseModel):
    """Chat message with optional tool calls"""
    role: str
    content: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None
    reasoning: Optional[str] = None


class ChatCompletionResponseChoice(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    index: int
    message: Union[Dict[str, Any], ChatMessage]
    finish_reason: Optional[str] = "stop"


class ChatCompletionResponseUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[ChatCompletionResponseChoice]
    usage: ChatCompletionResponseUsage


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Dict[str, Any]]
    temperature: Optional[float] = 1.0
    tools: Optional[List[Dict[str, Any]]] = None
    tool_choice: Optional[Union[str, Dict[str, Any]]] = None
    top_p: Optional[float] = 1.0
    n: Optional[int] = 1
    stream: Optional[bool] = False
    stop: Optional[Union[str, List[str]]] = None
    response_format: Optional[Dict[str, Any]] = None
    max_tokens: Optional[int] = None
    presence_penalty: Optional[float] = 0.0
    frequency_penalty: Optional[float] = 0.0
    user: Optional[str] = None


class ModelResponse(BaseModel):
    id: str
    object: str = "model"
    created: int
    owned_by: str = "organization-name"
    context_window: Optional[int] = None
    max_output_tokens: Optional[int] = None


class ModelListResponse(BaseModel):
    object: str = "list"
    data: List[ModelResponse]


class ResponseInputContentPart(BaseModel):
    """Typed content parts for Responses API inputs."""
    type: Literal["input_text", "text", "output_text"]
    text: str
    annotations: Optional[List[Dict[str, Any]]] = None


class ResponseInputMessage(BaseModel):
    """Responses API message input item."""
    type: Literal["message"]
    role: str
    content: List[ResponseInputContentPart]


class ResponseInputText(BaseModel):
    """Responses API input_text item."""
    type: Literal["input_text"]
    text: str


class ResponseFunctionCall(BaseModel):
    """Responses API function_call input item."""
    type: Literal["function_call"]
    call_id: str
    name: str
    arguments: str


class ResponseFunctionCallOutput(BaseModel):
    """Responses API function_call_output input item."""
    type: Literal["function_call_output"]
    call_id: str
    output: str


ResponseInputItem = Union[
    ResponseInputMessage,
    ResponseInputText,
    ResponseFunctionCall,
    ResponseFunctionCallOutput,
]


class ResponseRequest(BaseModel):
    """OpenAI Responses API request model"""
    model: str
    input: Optional[Union[str, List[Union[ResponseInputItem, Dict[str, Any]]]]] = None
    messages: Optional[List[Dict[str, Any]]] = None
    input_content: Optional[str] = None
    input_type: Optional[str] = "text"  # or "files", "json"
    instructions: Optional[str] = None
    text: Optional[Dict[str, Any]] = None
    temperature: Optional[float] = 1.0
    top_p: Optional[float] = 1.0
    n: Optional[int] = 1
    stream: Optional[bool] = False
    stop: Optional[Union[str, List[str]]] = None
    max_tokens: Optional[int] = None
    max_output_tokens: Optional[int] = None
    presence_penalty: Optional[float] = 0.0
    frequency_penalty: Optional[float] = 0.0
    logit_bias: Optional[Dict[str, float]] = None
    user: Optional[str] = None
    tools: Optional[List[Dict[str, Any]]] = None
    tool_choice: Optional[Union[str, Dict[str, Any]]] = None


class ResponseOutputMessage(BaseModel):
    """Message output from a response"""
    role: str
    content: Optional[str] = None
    annotations: Optional[List[Dict[str, Any]]] = None


class ResponseOutputToolCall(BaseModel):
    """Tool call output from a response"""
    id: str
    type: str
    function: Dict[str, Any]


class ResponseOutputTextPart(BaseModel):
    """Text content part for Responses output items"""
    type: str = "output_text"
    text: str
    annotations: Optional[List[Dict[str, Any]]] = None


class ResponseOutputMessageItem(BaseModel):
    """Responses API message output item"""
    id: str
    type: str = "message"
    role: str = "assistant"
    content: List[ResponseOutputTextPart]
    reasoning: Optional[str] = None


class ResponseOutputFunctionCallItem(BaseModel):
    """Responses API function_call output item"""
    id: str
    type: str = "function_call"
    call_id: str
    name: str
    arguments: str


class ResponseOutput(BaseModel):
    """Output item from a response"""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    item: Any


class ResponseUsage(BaseModel):
    """Usage statistics for a response"""
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    prompt_tokens_details: Optional[Dict[str, Any]] = None
    completion_tokens_details: Optional[Dict[str, Any]] = None


class ResponseResponse(BaseModel):
    """Complete response from the API"""
    id: str
    object: str = "response"
    created_at: int
    model: str
    output: List[Any]
    usage: ResponseUsage
    status: str = "completed"
    role: str = "assistant"
    incomplete_details: Optional[Dict[str, Any]] = None
    warning: Optional[str] = None
