package com.github.shniu.im.core.util;

import com.github.shniu.im.core.CommonConstant;
import com.google.common.base.Joiner;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;

/**
 * @author niushaohan
 * @date 2021/1/6 13
 */
public final class StringUtil {
    private StringUtil() {
    }

    public static String join(final String... parts) {
        System.out.println(Arrays.toString(parts));
        return "hhh" + Arrays.toString(parts);
    }

    public static String join(final List<String> parts) {
        if (Objects.isNull(parts)) {
            return null;
        }

        return Joiner.on(CommonConstant.COMMA).join(parts);
    }
}
