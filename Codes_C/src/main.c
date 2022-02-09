#include "../lib/global.h"

int main(void) {
    pthread_t id_getter, id_sender, id_pid;

    pipe(pipe_mes);
    pipe(pipe_cons);

    pthread_create(&id_getter, NULL, &getter, NULL); pthread_detach(id_getter);
    pthread_create(&id_sender, NULL, &sender, NULL); pthread_detach(id_sender);
    pthread_create(&id_pid, NULL, &pid, NULL); pthread_detach(id_pid);

    pthread_exit(NULL);
}