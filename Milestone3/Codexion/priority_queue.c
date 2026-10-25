#include "codexion.h"


pthread_mutex_lock(&dongle->lock);
push_to_heap(&dongle->queue, my_id, my_priority_score);

while (dongle->is_held ||
        get_current_time() < dongle->available_at ||
        dongle->queue.requests[0].coder_id != my_id)
{
    pthread_cond_wait(&dongle->cv, &dongle->lock);
}

pop_from_heap(&dongle->queue);
dongle->is_held = 1;


pthread_mutex_unlock(&dongle->lock);

void    swap_requests(t_request *a, t_request   *b)
{
    t_request   temp = *a;
    *a = *b;
    *b = temp;
}

void    push_to_heap(t_pqueue   *q, int coder_id, long  priority_score)
{
    if (q->size >= q->capacity)
        return;

    int current = q->size;
    q->requests[current].coder_id = coder_id;
    q->requests[current].priority_score = priority_score;
    q->size++;
    int parent = (current - 1) / 2;


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
        {
            smallest = left_child;
        }

        if (right_child < q->size &&
            q->requests[right_child].priority_score < q->requests[smallest].priority_score)
        {
            smallest = right_child;
        }

        if (smallest == current)
            break;

        swap_requests(&q->requests[current], &q->requests[smallest]);
        current = smallest;
    }
}
