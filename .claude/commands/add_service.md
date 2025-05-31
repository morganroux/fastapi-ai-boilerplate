I need to add a new service to this FastAPI boilerplate project. Please help me create all the necessary files following the
  existing patterns and architecture.

  **Step 1: Service Requirements**
  First, ask me these questions:
  1. What is the name of the service? (e.g., "product", "notification", "payment")
  2. What will this service do? (brief description of its main functionality)
  3. What dependencies will this service need? (list any other services/repositories it should depend on)

  **Step 2: Analysis and Planning**
  After I provide the requirements, please:
  1. Scan the existing codebase to identify:
     - Current naming patterns in services/, repository/, models/, and routes/
     - Existing dependencies and imports
     - Database connection patterns
     - Container registration patterns

  2. Based on the service name I provide, suggest these file names and confirm with me:
     - Service file: `src/services/{service_name}_service.py`
     - Repository file: `src/repository/{service_name}_repository.py`
     - Route file: `src/routes/{service_name}s.py` (note the plural for routes)
     - Model classes: `{ServiceName}Model`, `{ServiceName}Create`, `{ServiceName}` (following the existing pattern)

  3. Create a comprehensive plan showing all files that will be created/modified:
     - New service interface and implementation
     - New repository interface and implementation
     - Model additions to `src/models/models.py`
     - Container registrations in `src/container/container.py`
     - Dependency injection updates in `src/container/dependencies.py`
     - New route file with CRUD endpoints
     - Main app registration in `src/main.py`

  **Step 3: Implementation Requirements**
  When implementing, follow these exact patterns from the existing codebase:

  **Service Pattern:**
  - Create both interface (ABC) and implementation classes
  - Use dependency injection for repositories
  - Follow the naming: `{ServiceName}ServiceInterface` and `{ServiceName}Service`
  - Include basic CRUD methods: create, get_by_id, get_all
  - Handle errors appropriately with ValueError for business logic

  **Repository Pattern:**
  - Create both interface (ABC) and implementation classes
  - Use DatabaseConnection dependency injection
  - Follow the naming: `{ServiceName}RepositoryInterface` and `{ServiceName}Repository`
  - Include basic CRUD methods using SQLAlchemy patterns
  - Use session management with `self.db_connection.get_session()`

  **Model Pattern:**
  - Add SQLAlchemy model class: `{ServiceName}Model` inheriting from Base
  - Add Pydantic schemas: `{ServiceName}Create` and `{ServiceName}`
  - Use appropriate column types and relationships
  - Follow the `from_attributes = True` pattern in Config

  **Container Pattern:**
  - Add private attributes for repository and service instances
  - Add getter methods with lazy initialization
  - Register dependencies properly in the DIContainer class
  - Update the global container function if needed

  **Route Pattern:**
  - Create APIRouter with prefix and tags
  - Implement standard CRUD endpoints (POST /, GET /{id}, GET /)
  - Use proper dependency injection with FastAPI Depends
  - Include proper HTTP status codes and error handling
  - Add docstrings for each endpoint

  **Dependencies:**
  - Add dependency functions in `src/container/dependencies.py`
  - Follow the pattern: `def get_{service_name}_service() -> {ServiceName}Service:`
  - Use the global container to resolve dependencies

  Please confirm the service details and suggested names before proceeding with implementation. Then implement all files
  following these exact patterns, ensuring consistency with the existing codebase architecture.
