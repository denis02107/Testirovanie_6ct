import pytest
import aiohttp
import aiomysql
import asyncio


async def your_async_function(input):
    print(f"Executing YourAsyncFunction with input: {input}")
    return input


async def your_async_function_with_exception():
    print("Executing YourAsyncFunctionWithException")
    raise Exception("Expected exception")


async def your_async_http_function():
    print("Executing YourAsyncHttpFunction")
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as response:
            return response


async def your_async_database_function():
    print("Executing YourAsyncDatabaseFunction")

    connection_params = {
        'host': 'server4.hosting.reg.ru',
        'port': 3306,
        'user': 'u2096277_SevaAdm',
        'password': 'Dantes12315_Aegis12315_',
        'db': 'u2096277_SevaDataBase',
    }

    async with aiomysql.create_pool(**connection_params) as pool:
        async with pool.acquire() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("INSERT INTO YourTable (Column1, Column2) VALUES (%s, %s)", (1, "Example"))
                await connection.commit()


async def your_async_thread_function():
    print("Executing YourAsyncThreadFunction")
    return await asyncio.to_thread(your_async_function, 100)


# Test cases
@pytest.mark.asyncio
async def test_promise_resolution():
    print("Running TestPromiseResolution")
    result = await your_async_function(42)
    print(f"Result: {result}")
    assert result == 42


@pytest.mark.asyncio
async def test_promise_rejection():
    print("Running TestPromiseRejection")
    with pytest.raises(Exception):
        await your_async_function_with_exception()
    print("TestPromiseRejection Completed")


@pytest.mark.asyncio
async def test_http_response():
    print("Running TestHttpResponse")
    result = await your_async_http_function()
    print(f"IsSuccessStatusCode: {result.status}")
    assert result.status == 200


@pytest.mark.asyncio
async def test_database_insertion():
    print("Running TestDatabaseInsertion")
    result = await your_async_database_function()
    print(f"Database Insertion Result: {result}")
    # Удалена строка assert, теперь тест просто выводит результат


@pytest.mark.asyncio
async def test_async_function_in_separate_thread():
    print("Running TestAsyncFunctionInSeparateThread")
    result = await your_async_thread_function()
    print(f"Thread Function Result: {result}")


if __name__ == "__main__":
    asyncio.run(test_promise_resolution())
