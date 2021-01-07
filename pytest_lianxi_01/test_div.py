import pytest

from pytest_lianxi_01.div import div1
from pytest_lianxi_01.div import div2


# pytest分组，要导报
# 代码如下：@pytest.mark.组名
# 分组的使用，需要在命令行使用如下代码：pytest -m 组名        pytest -m "组名"
@pytest.mark.zu01
def test_div_int():
    assert div1(10, 2) == 5

@pytest.mark.zu01
def test_div_float():
    assert div1(100.8, 2) == 50.4

@pytest.mark.zu02
def test_div_type():
    assert div1('aa', 123) == 0

@pytest.mark.zu03
def test_div_error():
    # 预期为异常需要用到该语句
    with pytest.raises(ZeroDivisionError):
        div1(10, 0)


# 参数化 需要用到pytest里面的方法。同样需要pytest包
@pytest.mark.parametrize('number1,number2,number3', {
    (10, 2, 5),
    (82722317636733, 1, 82722317636733),
    (1, 2, 7),
    (1223, 2, 611.5)
})
def test_div_par(number1, number2, number3):
    assert div1(number1, number2) == number3



