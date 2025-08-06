def solution(h1, m1, s1, h2, m2, s2):
    t_start = h1 * 3600 + m1 * 60 + s1
    t_end   = h2 * 3600 + m2 * 60 + s2

    k_min = (t_start * 59 + 3600 - 1) // 3600
    k_max = (t_end   * 59)         // 3600
    count_ms = max(0, k_max - k_min + 1)

    j_min = (t_start * 719 + 43200 - 1) // 43200
    j_max = (t_end   * 719)          // 43200
    count_sh = max(0, j_max - j_min + 1)

    triple = 0
    if t_start <= 0    <= t_end:  triple += 1
    if t_start <= 43200 <= t_end: triple += 1

    return count_ms + count_sh - triple