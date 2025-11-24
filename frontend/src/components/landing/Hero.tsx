import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ArrowRight, PlayCircle, CheckCircle2 } from "lucide-react";

export function Hero() {
    return (
        <div className="relative overflow-hidden bg-slate-950 pt-20 pb-32 lg:pt-32 lg:pb-40">
            {/* Background Effects */}
            <div className="absolute inset-0 bg-[url('/grid.svg')] bg-center [mask-image:linear-gradient(180deg,white,rgba(255,255,255,0))]" />
            <div className="absolute top-0 right-0 -translate-y-12 translate-x-12 blur-3xl opacity-20">
                <div className="aspect-[1155/678] w-[72.1875rem] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30" />
            </div>
            <div className="absolute bottom-0 left-0 translate-y-12 -translate-x-12 blur-3xl opacity-20">
                <div className="aspect-[1155/678] w-[72.1875rem] bg-gradient-to-tr from-[#4f46e5] to-[#80caff] opacity-30" />
            </div>

            <div className="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="grid lg:grid-cols-2 gap-16 items-center">
                    <div className="text-left">
                        <div className="inline-flex items-center rounded-full border border-blue-500/30 bg-blue-500/10 px-3 py-1 text-sm font-medium text-blue-400 mb-8 backdrop-blur-sm">
                            <span className="flex h-2 w-2 rounded-full bg-blue-400 mr-2 animate-pulse"></span>
                            Precision Animation Engine v2.0
                        </div>

                        <h1 className="text-5xl font-bold tracking-tight text-white sm:text-7xl mb-6 leading-tight">
                            Precision Animation is <br />
                            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-violet-400 to-indigo-400">
                                The Future.
                            </span>
                        </h1>

                        <p className="text-lg text-slate-400 mb-8 leading-relaxed max-w-xl">
                            Random AI video generation is inaccurate, hallucinated, and inexplainable.
                            <br /><br />
                            <span className="text-slate-200 font-medium">VidSimplify</span> generates precise, multi-dimensional animated videos explaining every detail in depth. Edit and repurpose exactly how you want.
                        </p>

                        <div className="flex flex-col sm:flex-row gap-4 mb-12">
                            <Link href="/app">
                                <Button size="lg" className="h-14 px-8 text-lg bg-blue-600 hover:bg-blue-500 text-white border-0 shadow-lg shadow-blue-500/25 w-full sm:w-auto">
                                    Start Creating <ArrowRight className="ml-2 h-5 w-5" />
                                </Button>
                            </Link>
                            <Button variant="outline" size="lg" className="h-14 px-8 text-lg border-slate-700 text-slate-300 hover:bg-slate-800 hover:text-white w-full sm:w-auto">
                                <PlayCircle className="mr-2 h-5 w-5" />
                                See the Difference
                            </Button>
                        </div>

                        <div className="flex items-center gap-8 text-slate-500 text-sm font-medium">
                            <div className="flex items-center gap-2">
                                <CheckCircle2 className="h-4 w-4 text-blue-500" />
                                <span>Mathematically Accurate</span>
                            </div>
                            <div className="flex items-center gap-2">
                                <CheckCircle2 className="h-4 w-4 text-blue-500" />
                                <span>Fully Editable Code</span>
                            </div>
                            <div className="flex items-center gap-2">
                                <CheckCircle2 className="h-4 w-4 text-blue-500" />
                                <span>No Hallucinations</span>
                            </div>
                        </div>
                    </div>

                    {/* Hero Visual */}
                    <div className="relative lg:h-[600px] w-full">
                        <div className="absolute inset-0 bg-gradient-to-tr from-blue-500/10 to-violet-500/10 rounded-2xl border border-white/10 backdrop-blur-sm p-2">
                            <div className="h-full w-full bg-slate-900/90 rounded-xl overflow-hidden relative group">
                                {/* Abstract UI Representation */}
                                <div className="absolute top-0 left-0 right-0 h-12 bg-slate-800/50 border-b border-white/5 flex items-center px-4 gap-2">
                                    <div className="h-3 w-3 rounded-full bg-red-500/20"></div>
                                    <div className="h-3 w-3 rounded-full bg-yellow-500/20"></div>
                                    <div className="h-3 w-3 rounded-full bg-green-500/20"></div>
                                </div>

                                <div className="absolute inset-0 flex items-center justify-center">
                                    <div className="relative w-64 h-64">
                                        {/* Animated Circles representing precision */}
                                        <div className="absolute inset-0 border-2 border-blue-500/30 rounded-full animate-[spin_10s_linear_infinite]"></div>
                                        <div className="absolute inset-4 border-2 border-violet-500/30 rounded-full animate-[spin_15s_linear_infinite_reverse]"></div>
                                        <div className="absolute inset-8 border-2 border-indigo-500/30 rounded-full animate-[spin_20s_linear_infinite]"></div>
                                        <div className="absolute inset-0 flex items-center justify-center">
                                            <div className="text-center">
                                                <div className="text-4xl font-bold text-white mb-2">100%</div>
                                                <div className="text-blue-400 text-sm tracking-widest uppercase">Precision</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                {/* Floating Cards */}
                                <div className="absolute bottom-8 left-8 right-8 bg-slate-800/80 backdrop-blur p-4 rounded-lg border border-white/10 transform translate-y-full group-hover:translate-y-0 transition-transform duration-500">
                                    <div className="flex items-center gap-4">
                                        <div className="h-10 w-10 rounded-lg bg-green-500/20 flex items-center justify-center text-green-400">
                                            <CheckCircle2 className="h-6 w-6" />
                                        </div>
                                        <div>
                                            <div className="text-white font-medium">Generation Complete</div>
                                            <div className="text-slate-400 text-sm">Rendered in 1080p60 • 0 hallucinations</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
