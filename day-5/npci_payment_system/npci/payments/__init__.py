"""
Payments package - all payment gateway implementations
"""

from .upi import UPIGateway
from .imps import IMPSGateway
from .neft import NEFTGateway

__all__ = ['UPIGateway', 'IMPSGateway', 'NEFTGateway']

# Gateway registry
AVAILABLE_GATEWAYS = {
    'UPI': UPIGateway,
    'IMPS': IMPSGateway,
    'NEFT': NEFTGateway
}

def get_gateway(gateway_type):
    """Factory function to get gateway instance"""
    gateway_class = AVAILABLE_GATEWAYS.get(gateway_type.upper())
    if gateway_class:
        return gateway_class()
    raise ValueError(f"Unknown gateway type: {gateway_type}")