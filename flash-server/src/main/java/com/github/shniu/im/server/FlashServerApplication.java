package com.github.shniu.im.server;

import com.github.shniu.im.core.IMBootstrap;
import com.github.shniu.im.core.IMConfiguration;
import com.github.shniu.im.server.handler.netty.EchoHandler;

/**
 * @author niushaohan
 * @date 2021/1/6 13
 */
public class FlashServerApplication {
    public static void main(String[] args) {
        IMConfiguration configuration = IMConfiguration.defaultBuilder();

        IMBootstrap imBootstrap = new IMServerBootstrap(configuration);

        // Init handlers
        imBootstrap.addHandler(EchoHandler.class);

        imBootstrap.start();
    }
}
