def test_hello_cfg(cfg):
    print(f"hello {cfg.test_hello.hello}!")

def test_hello_ctx(ctx):
    ctx.a = 1

def test_hello_ctx2(ctx):
    assert ctx.a == 1
