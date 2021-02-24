package com.github.shniu.im.server;

import com.github.shniu.im.core.IMBootstrap;
import com.github.shniu.im.core.IMConfiguration;
import com.github.shniu.im.core.InternalBootstrap;
import com.github.shniu.im.core.netty.NettyServerBootstrap;

import java.util.ArrayList;
import java.util.List;

/**
 * @author niushaohan
 * @date 2021/2/7 18
 */
public class IMServerBootstrap implements IMBootstrap {
    private IMConfiguration configuration;

    private List<Class<?>> handlers;

    public IMServerBootstrap(IMConfiguration configuration) {
        this.configuration = configuration;

        handlers = new ArrayList<>();
    }

    @Override
    public void start() {
        // Todo 根据配置来选择使用哪个底层的网络路
        String bootstrap = configuration.getBootstrap();

        InternalBootstrap internalBootstrap = new NettyServerBootstrap(configuration.getPort());

        // config handlers
        internalBootstrap.initHandler(handlers);

        internalBootstrap.start();
    }

    @Override
    public void addHandler(Class<?> handler) {
        this.handlers.add(handler);
    }
}
