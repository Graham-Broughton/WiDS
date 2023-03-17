from dataclasses import dataclass, field


@dataclass
class CFG:
    SEED: int = 42
    USE_BO: bool = True