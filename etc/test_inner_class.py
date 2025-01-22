
class TestOuterClass:
    def test_outer_class(self):
        # can test with pytest
        pass

    class InnerClass:
        def test_inner_class(self):
            # can't test with pytest
            pass