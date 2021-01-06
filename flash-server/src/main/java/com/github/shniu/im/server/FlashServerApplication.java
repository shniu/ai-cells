package com.github.shniu.im.server;

import com.github.shniu.im.core.CommonConstant;
import com.github.shniu.im.core.util.StringUtil;

/**
 * @author niushaohan
 * @date 2021/1/6 13
 */
public class FlashServerApplication {
    public static void main(String[] args) {
        System.out.println(CommonConstant.SERVER_WELCOME);

        // StringUtil.join(Lists.newArrayList("12", "34"));
        StringUtil.join("1", "2", "3");
    }
}
