import supy, ROOT as r
import calculables, samples

class stgcHitLook(supy.analysis) :
    
    def parameters(self) :
        fields =                    [ 'stgcSimhit',     ]
        objects =  dict(zip(fields, [('Hits_sTGC_',''), ]))
        return {
            'objects'  : objects,
            }

    def listOfSteps(self,config) :
        steps  = []
        steps += [supy.steps.printer.progressPrinter(),
                  supy.steps.histos.multiplicity('truthIndices', max=10),
                  supy.steps.histos.multiplicity('simhitIndices', max=50),
                  supy.steps.histos.multiplicity('IndicesOddSector', max=50),
                  supy.steps.histos.multiplicity('IndicesEvenSector', max=50),
                  ]
        return steps
    
    def listOfCalculables(self,config) :
        calcs  = supy.calculables.zeroArgs(supy.calculables)
        calcs += [calculables.truth.truthIndices(label=''),
                  calculables.stgc.simhitIndices(label=''),
                  ]
        return calcs
    
    def listOfSampleDictionaries(self) :
        return [samples.localsinglemu,]
    
    def listOfSamples(self,config) :
        return (supy.samples.specify(names="SingleMu", color=r.kBlack, markerStyle = 20)
                )

    
    def conclude(self,pars) :
        #make a pdf file with plots from the histograms created above
        org = self.organizer(pars)
        org.scale()
        supy.plotter(org,
                     pdfFileName = self.pdfFileName(org.tag),
                     ).plotAll()
