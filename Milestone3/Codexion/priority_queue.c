#include "codexion.h"

void    swap_requests(t_request *a, t_request   *b)
{
    t_request   temp;

    temp = *a;
    *a = *b;
    *b = temp;
}

void    push_to_heap(t_pqueue   *q, int coder_id, long  p_score)
{
    int current;
    int parent;

    if (q->size >= q->capacity)
        return;
    current = q->size;
    q->requests[current].coder_id = coder_id;
    q->requests[current].p_score = p_score;
    q->size++;
    parent = (current - 1) / 2;
    while (current > 0 && \
            q->requests[current].p_score < \
            q->requests[parent].p_score)
    {
        swap_requests(&q->requests[current], &q->requests[parent]);
        current = parent;
        parent = (current - 1) / 2;
    }
}

void    pop_from_heap(t_pqueue  *q)
{
    int current;
    int left;
    int right;
    int smallest;

    if (q->size <= 0)
        return;
    q->requests[0] = q->requests[q->size - 1];
    q->size--;
    current = 0;
    while (1)
    {
        left = 2 * current + 1;
        right = 2 * current + 2;
        smallest = current;
        if (left < q->size &&
            q->requests[left].p_score < q->requests[smallest].p_score)
            smallest = left;
        if (right < q->size &&
            q->requests[right].p_score < q->requests[smallest].p_score)
            smallest = right;
        if (smallest == current)
            break;
        swap_requests(&q->requests[current], &q->requests[smallest]);
        current = smallest;
    }
}