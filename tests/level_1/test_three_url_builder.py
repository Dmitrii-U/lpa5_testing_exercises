from functions.level_1.three_url_builder import build_url


def test_build_url(build_url_fxt):
    assert build_url(**build_url_fxt['param']) == build_url_fxt['result']
