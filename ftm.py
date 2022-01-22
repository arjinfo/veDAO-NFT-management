import dataclasses
import pandas as pd

from typing import Any, Dict, List, Optional, TypedDict, Union

@dataclasses.dataclass
class GasInfo: 
    """Transaction gas info in units of wei.
    
    Attributes: 
        gas_used_wei (int): Gas units (wei) used by the txn.
        gas_price_wei (int): Current Fantom gas price in wei.
        tx_hash (str): Fantom address of the transaction.
        tx_gas_cost_wei (int): Gas cost of the txn in units of wei.
        tx_gas_cost_ftm (float): Gas cost of the txn in units of FTM.
        ftm_price_usd (Optional[float]): Defaults to None.
        timestamp (Optional[pd.Timestamp]): Defaults to None.
    """
    gas_used_wei: int
    gas_price_wei: int
    tx_hash: str
    ftm_price_usd: Optional[float] = None
    timestamp: Optional[pd.Timestamp] = None

    @property
    def tx_gas_cost_wei(self) -> int:
        return self.gas_price_wei * self.gas_used_wei

    @property
    def tx_gas_cost_ftm(self) -> float:
        return wei2fantom(self.tx_gas_cost_wei)

def wei2gwei(wei: Union[str, int], from_base16: bool = False):
    """Converts wei to Gwei (giga wei)."""

    if not isinstance(wei, (str, int)):
        raise ValueError("")

    if from_base16:
        assert isinstance(wei, str)
        wei: int = int(wei, base=16)

    return wei / 1e9

def wei2fantom(wei: Union[str, int], from_base16: bool = False):
    """Converts units of wei to FTM (1e18 * wei)."""

    if not isinstance(wei, (str, int)):
        raise ValueError("")

    if from_base16:
        assert isinstance(wei, str)
        wei: int = int(wei, base=16)

    return wei / 1e18


def gwei2wei(gwei: Union[str, int], from_base16: bool = False):
    """Converts Gwei, the units of FTM, to wei."""

    if not isinstance(gwei, (str, int)):
        raise ValueError("")

    if from_base16:
        assert isinstance(gwei, str)
        gwei: int = int(gwei, base=16)

    return gwei * 1e9


def fantom2wei(fantom: float):
    """Converts units of wei to FTM (1e18 * wei)."""
    return fantom * 1e18