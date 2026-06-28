if __name__=="__main__":
        pass

print("\nExplore Module Attributes:");
module=input("\nEnter module name to explore:");
print(f"\nAvailable Attributes in {module} module:\n\n {dir(module)}");
print("\n\n");