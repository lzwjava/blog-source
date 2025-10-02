---
title: Optimized Clash Proxy Selection Performance
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
model: x-ai/grok-code-fast-1
---

ummary

  I optimized the Clash proxy selection scripts to avoid testing proxies that won't be selected anyway, significantly improving performance by reducing
  unnecessary speed tests.

  What Was Optimized

  The original code would:
  1. Test all available proxies for speed
  2. Then filter to only select SG/TW (or HK) proxies
  3. This wasted time testing proxies that would be discarded

  The Fix

  Modified get_top_proxies() in speed.py to accept a name_filter parameter and filter proxies before speed testing:

  def get_top_proxies(num_results=5, name_filter=None):
      """
      Tests Clash proxy speeds concurrently and returns the top N fastest individual proxies.

      Args:
          num_results (int): Number of top proxies to return (default: 5)
          name_filter (list): List of strings to filter proxy names. Only proxies containing
                             any of these strings in their name will be tested.
      """

  Performance Benefits

  - Reduced network requests: Only tests proxies you actually care about
  - Faster execution: No wasted time testing irrelevant proxies
  - Clearer logging: Shows exactly how many proxies were filtered

  Simplified Configuration

  Removed the --hk flag, now always tests only SG and TW proxies for maximum focus and simplicity.

  Results

  The optimization cut down execution time significantly since most proxies don't contain "SG" or "TW" in their names, making the speed testing phase much
  more efficient.