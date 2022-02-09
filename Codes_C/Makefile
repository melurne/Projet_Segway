CC=gcc
CFLAGS=-g -Wall -Wextra -O3
LFLAGS=-pthread

header_files := $(wildcard lib/*.h)

all: build/raspi

build/raspi: thread_f.o, main.o, pid.o
	$(CC) $(CFLAGS) $(LFLAGS) $^ -o $@

obj/thread_f.o: src/thread_f.c, header_files
	$(CC) $(CFLAGS) -c $< -o $@

obj/main.o: src/main.c, header_files
	$(CC) $(CFLAGS) -c $< -o $@

obj/pid.o: src/pid.c, header_files
	$(CC) $(CFLAGS) -c $< -o $@

clean :
	rm -f obj/*
	rm -f build/*