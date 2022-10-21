class AstromechDroid:
    pass


class MedicalDroid:
    pass


class BattleDroid:
    pass


class PilotDroid:
    pass


class SuperRobot(AstromechDroid, MedicalDroid, BattleDroid, PilotDroid):
    pass


print(issubclass(SuperRobot, AstromechDroid))
print(issubclass(SuperRobot, MedicalDroid))
print(issubclass(SuperRobot, BattleDroid))
print(issubclass(SuperRobot, PilotDroid))
