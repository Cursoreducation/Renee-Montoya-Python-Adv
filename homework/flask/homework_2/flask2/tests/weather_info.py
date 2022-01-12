from dataclasses import dataclass


@dataclass
class WeatherInfo:
    city: str
    time_zone: str
    cloud: int
    temp: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            city=data["location"]["name"],
            time_zone=data["location"]["tz_id"],
            cloud=data["current"]["cloud"],
            temp=data["current"]["temp_c"],
        )
