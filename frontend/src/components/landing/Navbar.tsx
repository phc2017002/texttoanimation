import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Video } from "lucide-react";

export function Navbar() {
    return (
        <nav className="border-b border-white/5 bg-slate-950/80 backdrop-blur-md sticky top-0 z-50">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="flex h-16 items-center justify-between">
                    <Link href="/" className="flex items-center space-x-2">
                        <div className="h-8 w-8 bg-blue-600 rounded-lg flex items-center justify-center text-white">
                            <Video className="h-5 w-5" />
                        </div>
                        <span className="text-xl font-bold text-white">VidSimplify</span>
                    </Link>

                    <div className="hidden md:flex items-center space-x-8">
                        <Link href="#features" className="text-sm font-medium text-slate-300 hover:text-white transition-colors">
                            Features
                        </Link>
                        <Link href="#showcase" className="text-sm font-medium text-slate-300 hover:text-white transition-colors">
                            Showcase
                        </Link>
                        <Link href="#pricing" className="text-sm font-medium text-slate-300 hover:text-white transition-colors">
                            Pricing
                        </Link>
                    </div>

                    <div className="flex items-center space-x-4">
                        <Link href="/login" className="text-sm font-medium text-slate-300 hover:text-white transition-colors">
                            Log in
                        </Link>
                        <Link href="/app">
                            <Button className="bg-blue-600 hover:bg-blue-500 text-white">Get Started</Button>
                        </Link>
                    </div>
                </div>
            </div>
        </nav>
    );
}
