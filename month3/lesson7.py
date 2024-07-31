from typing import Any

class Cars:
    def __init__(self,name,year,model ) -> None:
        self.name = name
        self.year = year
        self.model = model

        def __repr__(self,name,year,model):
            return f"{name}, {year}, {model}"

class Factory:
    def __init__(self,name, year,model) -> None:
        self.name = name
        self.year = year
        self.model = model
        self.new_car = []


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if args:
            for arg in args:
                if isinstance(arg, Factory):
                    self.new_car.append(arg)
    
    def __repr__(self) -> str:
        return f"name: {self.name} \nyear: {self.year} \nmodel: {self.model}"


kia=Factory(name="audi", year=2023,model="r8")
gm =Factory(name="bmw",year=2024,model="M5")

k9=Cars(name="kia",year=2024,model="k9")
k8 =Cars(name="kia", year=2021,model="k8")
kia(k9,k8)
print(kia.new_car)
