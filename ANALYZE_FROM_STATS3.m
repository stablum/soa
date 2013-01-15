% IMPORT_FROM_STATS
% drag & drop stats. import as column vectors
%---------------------------------
% countsteps ---> countinterations
% expnum ---> runnum
% meanedgesimportance
% stdedgesimportance
% numkills
% pathlength
% totalweight
%----------------------------------

% from columns to matrix using steps and expnum: rows=RUNS, columns=exp
% for each variable, take mean and 25/75%iles of each cycle
% make graphs var vs cycle
% make anova of [final] values
%----------------------------------
%% from columns to matrix using steps and runnum: rows=RUNS, columns=exp
runnum=runnum+1; % DO Once, better to FIX BEFORE
countiterations=countiterations+1;
%% PUT everything under the correct policy structure.
%%%%%%%%%%%%%
npol=2%%%%%%%  CHANGE ME CAREFULLY: 1= pro_poor, 2=pro_rich, 3=pro_poor
%%%%%%%%%%%%%
%%
max_num_steps=max(countiterations);
max_num_runs=max(runnum);
steps=[1:max_num_steps];
runs=[1:max_num_runs];
ss=0;
pol(npol).all_steps=[];pol(npol).all_p_l=[];pol(npol).all_std_imp=[];pol(npol).all_mean_imp=[];pol(npol).all_n_kill=[];pol(npol).all_tot_w=[];
for col= runs
    for row=steps
        ss=ss+1;
            pol(npol).all_p_l(row,col)=pathlength(ss);
            pol(npol).all_std_imp(row,col)=stdedgesimportance(ss);
            pol(npol).all_mean_imp(row,col)=meanedgesimportance(ss);
            pol(npol).all_n_kill(row,col)=numkills(ss);
            pol(npol).all_tot_w(row,col)=totalweight(ss);
            pol(npol).all_steps(row,col)=countiterations(ss);
    end
end
%% for each variable, take mean and 25/75%iles of each cycle

pol(npol).p_l.p25=prctile(pol(npol).all_p_l',25);    pol(npol).std_imp.p25=prctile(pol(npol).all_std_imp',25);    pol(npol).mean_imp.p25=prctile(pol(npol).all_mean_imp',25);  pol(npol).n_kill.p25=prctile(pol(npol).all_n_kill',25);  pol(npol).tot_w.p25=prctile(pol(npol).all_tot_w',25);       
pol(npol).p_l.p75=prctile(pol(npol).all_p_l',75);    pol(npol).std_imp.p75=prctile(pol(npol).all_std_imp',75);    pol(npol).mean_imp.p75=prctile(pol(npol).all_mean_imp',75);  pol(npol).n_kill.p75=prctile(pol(npol).all_n_kill',75);   pol(npol).tot_w.p75=prctile(pol(npol).all_tot_w',75);     
pol(npol).p_l.avg=mean(pol(npol).all_p_l');          pol(npol).std_imp.avg=mean(pol(npol).all_std_imp');             pol(npol).mean_imp.avg=mean(pol(npol).all_mean_imp');         pol(npol).n_kill.avg=mean(pol(npol).all_n_kill');          pol(npol).tot_w.avg=mean(pol(npol).all_tot_w');          

%% make graphs variable (mean,25 and 75 percentile) x cycle
npol=2
cols=[0,0,1; 1,0,0; 0,0,0];

figure(1);
p1=plot(steps,pol(npol).p_l.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).p_l.p25,'--','color',cols(npol,:)); hold on;
p3=plot(steps,pol(npol).p_l.p75,'--','color',cols(npol,:)); hold on;  
title('path length over cycles')
ylabel('path length'); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

figure(2);
p1=plot(steps,pol(npol).std_imp.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).std_imp.p25,'--','color',cols(npol,:)); hold on; 
p3=plot(steps,pol(npol).std_imp.p75,'--','color',cols(npol,:)); hold on;  
title('stand deviation of the importance of the edges over the cycles');
ylabel('std dev of edge importance'); xlabel('cycles'); legend([p1,p2,p3],'mean','pile25','pile75')

figure(3);
p1=plot(steps,pol(npol).mean_imp.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).mean_imp.p25,'--','color',cols(npol,:)); hold on; 
p3=plot(steps,pol(npol).mean_imp.p75,'--','color',cols(npol,:)); hold on;  
title('mean edge importance over cycles')
ylabel('mean edge importance'); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

figure(4);
p1=plot(steps,pol(npol).n_kill.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).n_kill.p25,'--','color',cols(npol,:)); hold on; 
p3=plot(steps,pol(npol).n_kill.p75,'--','color',cols(npol,:)); hold on;  
title('number of dead edges over cycles')
ylabel('number of dead edges '); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')

figure(5);
p1=plot(steps,pol(npol).tot_w.avg,'color',cols(npol,:)); hold on;
p2=plot(steps,pol(npol).tot_w.p25,'--','color',cols(npol,:)); hold on;
p3=plot(steps,pol(npol).tot_w.p75,'--','color',cols(npol,:)); hold on;
title('total weight of the graph over cycles')
ylabel('total weight of the graph'); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75');

%% make cumulative of killed edges x cycle

figure;
p1=plot(steps,cumsum(pol(npol).n_kill.avg),'color',cols(npol,:)); hold on;
p2=plot(steps,(pol(npol).n_kill.p25),'--','color',cols(npol,:)); hold on;
p3=plot(steps,cumsum(pol(npol).n_kill.p75),'--','color',cols(npol,:)); hold on;  
title('cumulative number of dead edges over cycles')
ylabel('cumulative number of dead edges '); xlabel('cycles');legend([p1,p2,p3],'mean','pile25','pile75')


%% semilog plots
figure; semilogy(steps,pol(npol).p_l.avg)
%%  curve fitting
cftool(steps,pol(npol).std_imp.avg) % generated:

[fitresult, gof] = createexpFit(steps,pol(npol).p_l.avg,'path length')
[fitresult, gof] = createexpFit(steps,pol(npol).tot_w.avg,'total graph weight')
[fitresult, gof] = createexpFit(steps,pol(npol).std_imp.avg,'std dev of edges importance')

cftool(steps,pol(npol).tot_w.avg) % generated:

%% a detailed graph

npol=2
cols=[0,0,1; 1,0,0; 0,0,0];

figure(1);
b1=plot(steps,pol(1).p_l.avg,'color',cols(1,:)); hold on;
b2=plot(steps,pol(1).p_l.p25,'--','color',cols(1,:)); hold on;
b3=plot(steps,pol(1).p_l.p75,'--','color',cols(1,:)); hold on; 

r1=plot(steps,pol(2).p_l.avg,'color',cols(2,:)); hold on;
r2=plot(steps,pol(2).p_l.p25,'--','color',cols(2,:)); hold on;
r3=plot(steps,pol(2).p_l.p75,'--','color',cols(2,:)); hold on; 
title('path length over cycles')
ylabel('path length'); xlabel('cycles');legend([b1,b2,b3],'mean','pile25','pile75');
legend([b1,r1],'pro poor','pro rich')

%% make anova of [final] values
countsteps

runnum

meanedgesimportance

stdedgesimportance

numkills

pathlength

totalweight