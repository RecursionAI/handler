# handler
OpenAI compatible API with built in model routing and pipeline management.


## Routing
Create routes that are stored in a connected db. Handler will pull from those
routes and pass each request to each model, catching the [DONE] sequence and handing the request to the next model in 
the sequence until the route is complete.

Alternatively it can also be configured with a selector model that receives the request as well as a list of available
models and details on them and select the appropriate model for the job.


## Configuration

Routes are either **Pipelines** or **Ideal Model Selection** and can be configured and stored in the db.

Models can be added to pipelines, given descriptions, and given custom system prompts to perform specific tasks with
incoming request data i.e. summarize this task before handing it to Qwen3 Coder Next.


## Interaction
The APIs behave exactly like a normal OpenAI compatible API with proper chat streaming and SSE events but multiple
models can be used in a single request.