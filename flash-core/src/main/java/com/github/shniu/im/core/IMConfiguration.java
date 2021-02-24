package com.github.shniu.im.core;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;

/**
 * @author niushaohan
 * @date 2021/2/7 18
 */
@AllArgsConstructor
// @NoArgsConstructor
@Getter
@Builder
public final class IMConfiguration {

    /**
     * 监听端口.
     */
    private int port;

    /**
     * 网络框架的选择.
     */
    private final String bootstrap;
    // private final String bootstrap = "com.github.shniu.im.core.FlashNIOServerBootstrap";

    public static IMConfiguration defaultBuilder() {
        return IMConfiguration.builder()
                .bootstrap("com.github.shniu.im.core.netty.NettyServerBootstrap")
                .port(2000)
                .build();
    }
}
