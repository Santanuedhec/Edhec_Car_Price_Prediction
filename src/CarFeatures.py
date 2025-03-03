from pydantic import BaseModel, Field, field_validator

class CarFeatures(BaseModel):
    Levy: int = Field(..., ge=300, le=1500)
    Engine_volume: float = Field(..., ge=1, le=4)
    Mileage: int = Field(..., ge=0, le=330000)
    Cylinders: int = Field(..., ge=3, le=8)
    Doors: int = Field(..., ge=2, le=5)
    Airbags: int = Field(..., ge=0, le=16)
    Age: int = Field(..., ge=1, le=70)

    Leather_interior: int = Field(..., ge=0, le=1)
    Turbo: int = Field(..., ge=0, le=1)

    Wheel: str
    Drive_wheels: str
    Gear_box_type: str
    Fuel_type: str
    Color: str

    @field_validator("Wheel")
    def validate_wheel(cls, value):
        allowed = ["Left wheel", "Right-hand drive"]
        if value not in allowed:
            raise ValueError(f"Wheel must be one of {allowed}")
        return value

    @field_validator("Drive_wheels")
    def validate_drive_wheels(cls, value):
        allowed = ["4x4", "Front", "Rear"]
        if value not in allowed:
            raise ValueError(f"Drive_wheels must be one of {allowed}")
        return value

    @field_validator("Gear_box_type")
    def validate_gear_box(cls, value):
        allowed = ["Automatic", "Manual", "Tiptronic", "Variator"]
        if value not in allowed:
            raise ValueError(f"Gear_box_type must be one of {allowed}")
        return value

    @field_validator("Fuel_type")
    def validate_fuel_type(cls, value):
        allowed = ["CNG", "Diesel", "Hybrid", "Hydrogen", "LPG", "Petrol", "Plug-in Hybrid"]
        if value not in allowed:
            raise ValueError(f"Fuel_type must be one of {allowed}")
        return value

    @field_validator("Color")
    def validate_color(cls, value):
        allowed = [
            "Beige", "Black", "Blue", "Brown", "Carnelian red", "Golden",
            "Green", "Grey", "Orange", "Pink", "Purple", "Red",
            "Silver", "Sky blue", "White", "Yellow"
        ]
        if value not in allowed:
            raise ValueError(f"Color must be one of {allowed}")
        return value
