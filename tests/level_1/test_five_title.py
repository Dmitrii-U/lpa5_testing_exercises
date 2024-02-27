from functions.level_1.five_title import change_copy_item


def test_change_copy_item(ch_cp_item_fxt):
    assert change_copy_item(**ch_cp_item_fxt['param']) == ch_cp_item_fxt['result']
