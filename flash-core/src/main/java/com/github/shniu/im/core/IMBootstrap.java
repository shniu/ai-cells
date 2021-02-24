package com.github.shniu.im.core;

/**
 * @author niushaohan
 * @date 2021/2/7 18
 */
public interface IMBootstrap {
    void start();

    void addHandler(Class<?> handler);
}
