import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def dut_test(dut):
    assert 0, "Testing assertion"
    pass
