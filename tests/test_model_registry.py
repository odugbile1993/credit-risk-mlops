from src.model_registry import get_models

models = get_models()

print()

print("OPENFRAUDLABS MODEL REGISTRY")
print("-" * 50)

for name in models:

    print(name)