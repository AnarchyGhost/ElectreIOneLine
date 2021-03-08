def electreI(matrix, weights, agree_norm=0.5, disagree_norm=0.5, names=None):
    """
    Метод Electre I
    :param matrix: матрица, заданная в формате: строки- критерии, столбцы- альтернативы
    :param weights: ветор весов критериев
    :param agree_norm: пороговое значение индекса согласия, по умолчанию равен 0.5
    :param disagree_norm: пороговое значение индекса несогласия , по умолчанию равен 0.5
    :param names: ветор имен, по умолчанию None
    :return: вектор имен/номеров лучших альтернатив
    """
    return np.arange(0, matrix.shape[1])[((np.min((np.array([np.sum(weights[(matrix.transpose() / np.linalg.norm(
        matrix.transpose(), axis=0, keepdims=True))[i] >= (matrix.transpose() / np.linalg.norm(matrix.transpose(),
                                                                                               axis=0, keepdims=True))[
                                                                                j]]) for i in range(
        (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True)).shape[0]) for j in range(
        (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True)).shape[0])]).reshape(((
                                                                                                                      matrix.transpose() / np.linalg.norm(
                                                                                                                  matrix.transpose(),
                                                                                                                  axis=0,
                                                                                                                  keepdims=True)).shape[
                                                                                                                  0], (
                                                                                                                      matrix.transpose() / np.linalg.norm(
                                                                                                                  matrix.transpose(),
                                                                                                                  axis=0,
                                                                                                                  keepdims=True)).shape[
                                                                                                                  0]))
                                                   ), axis=1)) > agree_norm) & ((np.max((np.array([np.max(np.append(
        (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True))[j][
            (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True))[i] <
            (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True))[j]] -
        (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True))[i][
            (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True))[i] <
            (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True))[j]], 0)) for i in range(
        (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True)).shape[0]) for j in range(
        (matrix.transpose() / np.linalg.norm(matrix.transpose(), axis=0, keepdims=True)).shape[0])]).reshape(((
                                                                                                                      matrix.transpose() / np.linalg.norm(
                                                                                                                  matrix.transpose(),
                                                                                                                  axis=0,
                                                                                                                  keepdims=True)).shape[
                                                                                                                  0], (
                                                                                                                      matrix.transpose() / np.linalg.norm(
                                                                                                                  matrix.transpose(),
                                                                                                                  axis=0,
                                                                                                                  keepdims=True)).shape[
                                                                                                                  0]))
                                                                                         ), axis=1)) < disagree_norm)]
