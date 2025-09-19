package org.lzwjava;

import org.apache.commons.lang3.RandomStringUtils;

public class TraceIdGenerator {

    public static String generateTraceId() {
        return RandomStringUtils.randomAlphanumeric(6);
    }
}
