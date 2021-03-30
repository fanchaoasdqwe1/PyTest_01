from Requests_lianxi.test_qiyeweixin.api.department import Department


class TestDepartment:
    def setup(self):
        self.department = Department()

    # 创建一个部门
    def test_create(self):
        r = self.department.create('hello', 1)
        print(r)
        assert r["errcode"] == 0

    # 修改一个部门
    def test_update(self):
        r = self.department.update(4, name='hahahahaha')
        print(r)
        assert r["errcode"] == 0

    # 删除一个部门
    def test_delete(self):
        r = self.department.delete(4)
        print(r)
        assert r["errcode"] == 0

    # 获取部门列表
    def test_get(self):
        r = self.department.get(1)
        print(r)
        assert r["errcode"] == 0
