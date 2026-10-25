#include "codexion.h"

void    swap_requests(t_request *a, t_request   *b)
{
    t_request   temp = *a;
    *a = *b;
    *b = temp;
}

void    push_to_heap(t_pqueue   *q, int coder_id, long  priority_score)
{
    int current;
    int parent;


    if (q->size >= q->capacity)
        return;

    current = q->size;
    q->requests[current].coder_id = coder_id;
    q->requests[current].priority_score = priority_score;
    q->size++;
    parent = (current - 1) / 2;


    while (current > 0 && q->requests[current].priority_score < q->requests[parent].priority_score)
    {
        swap_requests(&q->requests[current], &q->requests[parent]);

        current = parent;
        parent = (current - 1) / 2;
    }
}

void    pop_from_heap(t_pqueue  *q)
{
    if (q->size <= 0)
        return;

    q->requests[0] = q->requests[q->size - 1];
    q->size--;
    int current = 0;


    while (1)
    {
        int left_child = 2 * current + 1;
        int right_child = 2 * current + 2;
        int smallest = current;


        if (left_child < q->size &&
            q->requests[left_child].priority_score < q->requests[smallest].priority_score)
            smallest = left_child;

        if (right_child < q->size &&
            q->requests[right_child].priority_score < q->requests[smallest].priority_score)
            smallest = right_child;

        if (smallest == current)
            break;

        swap_requests(&q->requests[current], &q->requests[smallest]);
        current = smallest;
    }
}