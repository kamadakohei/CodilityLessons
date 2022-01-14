def solution(X, A):
    # 場所ごとに葉が落ちたかどうかを覚えておくリスト
    fallenAt = [False] * (X+1)
    # 葉で埋まっている場所の数
    numFallen = 0
    #iはAのインデックス(=時間)
    for i in range(0, len(A)):
        # 落ちてきた葉の場所
        j = A[i]
        # その葉が、まだ葉が落ちていなかった場所に落ちたか
        if not fallenAt[j]:
            # その場所に葉があることを覚えておく
            fallenAt[j] = True
            # 新たに葉で埋まった場所の数をカウント
            numFallen += 1
        # 全部埋まったのなら終了
        if numFallen == X:
            return i
    # Aを全部なめても全ての場所が埋まらない
    return -1
