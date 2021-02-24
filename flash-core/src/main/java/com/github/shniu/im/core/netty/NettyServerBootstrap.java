package com.github.shniu.im.core.netty;

import com.github.shniu.im.core.InternalBootstrap;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.util.internal.ReflectionUtil;

import java.net.InetSocketAddress;
import java.util.ArrayList;
import java.util.List;

/**
 * @author niushaohan
 * @date 2021/2/7 18
 */
public class NettyServerBootstrap implements InternalBootstrap {
    private ServerBootstrap serverBootstrap;
    private InetSocketAddress inetSocketAddress;

    private List<Class<? extends ChannelHandler>> handlers;

    public NettyServerBootstrap(int port) {
        this.serverBootstrap = new ServerBootstrap();

        this.inetSocketAddress = new InetSocketAddress(port);
        this.handlers = new ArrayList<>();
    }

    @Override
    public void start() {
        EventLoopGroup bossGroup = new NioEventLoopGroup(1);
        EventLoopGroup workerGroup = new NioEventLoopGroup();

        serverBootstrap.group(bossGroup, workerGroup)
                .channel(NioServerSocketChannel.class)
                .childHandler(new ChannelInitializer<NioSocketChannel>() {
                    @Override
                    protected void initChannel(NioSocketChannel ch) throws Exception {
                        for (Class<? extends ChannelHandler> handler : handlers) {
                            ChannelHandler h = handler.newInstance();
                            ch.pipeline().addLast(h);
                        }
                    }
                });

        try {
            ChannelFuture f = serverBootstrap.bind(this.inetSocketAddress).sync();
            f.addListener(future -> {
                if (future.isSuccess()) {
                    System.out.println("Server start succeed.");
                } else {
                    System.out.println("Server start failure.");
                }
            });

            f.channel().closeFuture().sync();
        } catch (Exception e) {
            //
        } finally {
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }

    @SuppressWarnings("unchecked")
    public void initHandler(List<Class<?>> handlers) {
        for (Class<?> handler : handlers) {
            if (ChannelHandler.class.isAssignableFrom(handler)) {
                this.handlers.add((Class<? extends ChannelHandler>) handler);
            } else {
                System.out.println(handler + " is not assign from ChannelHandler, discard it.");
            }
        }

        if (this.handlers.isEmpty()) {
            System.out.println("handlers is empty, are you sure ?");
        }
    }
}
