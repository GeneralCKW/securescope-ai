"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import api from "../lib/api";
import { setToken } from "../lib/auth";

export default function LoginPage() {
    const router = useRouter();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError("");
        try {
            const form = new URLSearchParams();
            form.append("username", email);
            form.append("password", password);

            const res = await api.post("/auth/login", form, {
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
            });
            setToken(res.data.access_token);
            router.push("/dashboard");
        } catch {
            setError("Invalid email or password");
        } finally {
            setLoading(false);
        }
    };

return (
    <div className="min-h-screen flex items-center justify-center bg-zinc-50 dark:bg-zinc-900">
        <div className="w-full max-w-md bg-white dark:bg-zinc-800 rounded-2x1 shadow-sm p-8">
            <h1 className="text-2x1 front-semibold text-zinc-900 dark:text-white mb-2">
                SecureScope AI
            </h1>
            <p className="text-zinc-500 dark:text-zinc-400 mb-8">
                Sign in to your account
            </p>

            {error && (
                <div className="mb-4 p-3 rounded-lg bg-red-50 text-red-600 text-sm">
                    {error}
                </div>
            )}

            <form onSubmit={handleLogin} className="flex flex-col gap-4">
                <div>
                    <label className="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-1">
                        Email
                    </label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        className="w-full px-4 py-2 rounded-lg border border-zinc-200 dark:text-zinc-300 mb-1">
                        placeholder="you@example.com"
                    </input>
                </div>
                <div>
                    <label className="block text-sm font-medium text-zinc-700 dark:text-zinc-300 mb-1">
                        Password
                    </label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="w-full -px-4 py-2 rounded-lg border border-zinc-200 dark:border-zinc-700 bg-white dark:bd-zinc-900 text-zinc-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-zinc-400">
                        placeholder="••••••••"
                    </input>
                </div>
                <button
                    type="submit"
                    disabled={loading}
                    className="mt-2 w-full py-2 px-4 bg-zinc-900 dark:bg-white text-white dark:text-zinc-900 font-medium rounded-lg hover:bg-zinc-700 dark:hover:bg-zinc-200 transition-colors disabled:opacity-50">
                    {loading ? "Signing in..." : "Sign In"}    
                </button>
            </form>

            <p className="mt-6 text-center text-sm text-zinc-500">
                Don&apos;t have an account?{" "}
                <a href="/register" className="font-medium text-zinc-900 dark:text-white hover:underline">
                    Register
                </a>
            </p>
        </div>
    </div>
);
}