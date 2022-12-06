#!/usr/bin/env python3

signal = open("06.txt").read().strip()


def search_for_packet(signal, window_size):
    for i in range(len(signal)):
        window = signal[i : i + window_size]
        if len(window) == len(set(window)):
            # i starts from 0, but is included in window_size
            print(i + window_size, window)
            return i + window_size


search_for_packet(signal, 4)
search_for_packet(signal, 14)
