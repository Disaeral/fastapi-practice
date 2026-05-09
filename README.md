## This project was created in educational purposes

# Architecture
Tried to follow clean/layered arch in the implementation with separation of concerns between domain and implementation.
Right now flow goes as:
- request comes to one of the router handlers
- handler has service bound via DI container (dishka)
- service class calls repository methods

from service level interaction has abstract backbone + type hints used to describe available processing
- service -> defined abstract service 
- repo -> defined abstract repo

this approach has a few flaws one of which is a large boilerplate and not complete following of clean code/layered arch principles:
- `core/services/` are interfaces but `infrastructure/services/` are implementations — but there are no use cases
  right now services of infra(implementation level) encloses the use case logic that ideally should be separate
- api handlers should not use services directly but depend on use-case entities instead
  ```python
    @router.post("/users")
    async def create_user(use_case: CreateUserUseCase = Depends(...)): # Depends here is crucial(?)
      return await use_case.execute(...)
  ```
- mappers in implementation level cover both domain to orm conversion and vice-versa. should be separate?

# Should be done
no matter what auth mech will be used,
right now dependency injection flow is unclear to me. ideally, all request params should be handled as Depends:
example without explicit dependency injection container:
```python
    @router.get("/")
    def route(
        auth_username: str = Depends(get_auth_user_username),
        db: Session = Depends(get_db),                       
        current_user: User = Depends(get_current_user),      
    ):
```

fix how dishka used to also handle request params?
use pure depends?

implement jwt auth
