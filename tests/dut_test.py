import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def dut_test(dut):
    assert 1, "Testing asssertion"
    pass
