#!/usr/bin/env python3.5
#
# Copyright (c) 2016 by Ron Frederick <ronf@timeheart.net>.
# All rights reserved.
#
# This program and the accompanying materials are made available under
# the terms of the Eclipse Public License v1.0 which accompanies this
# distribution and is available at:
#
#     http://www.eclipse.org/legal/epl-v10.html
#
# Contributors:
#     Ron Frederick - initial implementation, API, and documentation

import asyncio, asyncssh, sys

async def run_client():
    async with asyncssh.connect('localhost') as conn:
        async with conn.create_process('bc') as process:
            for op in ['2+2', '1*2*3*4', '2^32']:
                process.stdin.write(op + '\n')
                result = await process.stdout.readline()
                print(op, '=', result, end='')

try:
    asyncio.get_event_loop().run_until_complete(run_client())
except (OSError, asyncssh.Error) as exc:
    sys.exit('SSH connection failed: ' + str(exc))
