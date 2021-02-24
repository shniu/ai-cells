package com.github.shniu.im.core;

import java.util.List;

/**
 * @author niushaohan
 * @date 2021/2/7 19
 */
public interface InternalBootstrap {
    void start();

    void initHandler(List<Class<?>> handlers);
}
